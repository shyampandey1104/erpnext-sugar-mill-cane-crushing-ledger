"""Sugar Mill Sugarcane Crushing, Recovery % & Statutory Farmer FRP Ledger."""

from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field


@dataclass
class CanePurchaseSlip:
    ticket_id: str
    farmer_id: str
    farmer_name: str
    cane_variety: str  # CO-0238, CO-86032
    cane_weight_metric_tonnes: float
    sugar_recovery_percentage: float  # e.g., 10.25%
    base_frp_rate_per_mt: float  # Central Govt FRP (e.g., ₹3,400/MT for 10.25% recovery)
    premium_for_excess_recovery: float
    total_cane_cost_payable_inr: float


@dataclass
class DailyCrushingShiftReport:
    shift_date: str
    total_cane_crushed_mt: float
    average_recovery_pct: float
    total_sugar_bags_produced_50kg: int
    molasses_recovery_mt: float
    bagasse_produced_mt: float


class SugarMillCaneEngine:
    """Sugar mill weighing slip, juice pol/brix lab recovery calculation, and farmer FRP payout engine."""

    BENCHMARK_RECOVERY_PCT = 10.25
    PREMIUM_PER_0_1PCT_RECOVERY = 33.20  # Additional per MT for every 0.1% recovery above benchmark

    def compute_cane_purchase_slip(
        self,
        ticket_id: str,
        farmer_id: str,
        farmer_name: str,
        variety: str,
        weight_mt: float,
        recovery_pct: float,
        base_frp_mt: float = 3400.0
    ) -> CanePurchaseSlip:
        if recovery_pct > self.BENCHMARK_RECOVERY_PCT:
            excess_steps = (recovery_pct - self.BENCHMARK_RECOVERY_PCT) / 0.10
            premium_per_mt = round(excess_steps * self.PREMIUM_PER_0_1PCT_RECOVERY, 2)
        else:
            premium_per_mt = 0.0

        final_rate_per_mt = base_frp_mt + premium_per_mt
        total_payable = round(weight_mt * final_rate_per_mt, 2)

        return CanePurchaseSlip(
            ticket_id=ticket_id,
            farmer_id=farmer_id,
            farmer_name=farmer_name,
            cane_variety=variety,
            cane_weight_metric_tonnes=weight_mt,
            sugar_recovery_percentage=recovery_pct,
            base_frp_rate_per_mt=base_frp_mt,
            premium_for_excess_recovery=premium_per_mt,
            total_cane_cost_payable_inr=total_payable
        )

    def generate_shift_production(
        self,
        shift_date: str,
        total_crushed_mt: float,
        avg_recovery_pct: float
    ) -> DailyCrushingShiftReport:
        sugar_produced_mt = (total_crushed_mt * avg_recovery_pct) / 100.0
        bags = int((sugar_produced_mt * 1000.0) / 50.0) # 50 kg bags
        molasses_mt = round(total_crushed_mt * 0.045, 2)  # ~4.5% molasses yield
        bagasse_mt = round(total_crushed_mt * 0.30, 2)    # ~30% bagasse yield for cogeneration

        return DailyCrushingShiftReport(
            shift_date=shift_date,
            total_cane_crushed_mt=total_crushed_mt,
            average_recovery_pct=avg_recovery_pct,
            total_sugar_bags_produced_50kg=bags,
            molasses_recovery_mt=molasses_mt,
            bagasse_produced_mt=bagasse_mt
        )
