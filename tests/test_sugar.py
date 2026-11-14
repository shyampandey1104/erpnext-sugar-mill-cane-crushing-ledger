import unittest
from sugar.engine import SugarMillCaneEngine

class TestSugarMill(unittest.TestCase):
    def test_farmer_frp_calculation_with_recovery_premium(self):
        engine = SugarMillCaneEngine()
        slip = engine.compute_cane_purchase_slip(
            ticket_id="CANE-2026-9001",
            farmer_id="FRM-UP-102",
            farmer_name="Chaudhary Charan Singh",
            variety="CO-0238",
            weight_mt=25.0, # 25 Metric Tonnes
            recovery_pct=10.45, # 0.20% above benchmark 10.25%
            base_frp_mt=3400.0
        )

        # 0.20% excess = 2 steps of 0.1% -> 2 * 33.20 = 66.40
        self.assertEqual(slip.premium_for_excess_recovery, 66.40)
        # Rate = 3466.40 * 25 = 86,660.0
        self.assertEqual(slip.total_cane_cost_payable_inr, 86660.0)

    def test_daily_crushing_shift_production(self):
        engine = SugarMillCaneEngine()
        prod = engine.generate_shift_production(
            shift_date="2026-11-14",
            total_crushed_mt=5000.0,
            avg_recovery_pct=11.0 # 550 MT sugar
        )
        self.assertEqual(prod.total_sugar_bags_produced_50kg, 11000)
        self.assertEqual(prod.molasses_recovery_mt, 225.0)
        self.assertEqual(prod.bagasse_produced_mt, 1500.0)

if __name__ == "__main__":
    unittest.main()
