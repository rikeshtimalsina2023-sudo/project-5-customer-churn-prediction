"""Smoke tests for the Streamlit churn-prediction dashboard."""

from pathlib import Path
import unittest

from streamlit.testing.v1 import AppTest


APP_PATH = Path(__file__).resolve().parents[1] / "app" / "dashboard.py"


class DashboardTests(unittest.TestCase):
    def test_dashboard_loads_and_predicts(self):
        app = AppTest.from_file(str(APP_PATH), default_timeout=30)
        app.run()
        self.assertEqual([], list(app.exception))
        self.assertEqual(["Predict Churn"], [button.label for button in app.button])

        app.button[0].click().run()

        self.assertEqual([], list(app.exception))
        self.assertEqual(
            ["Churn probability", "Prediction"],
            [metric.label for metric in app.metric],
        )
        self.assertRegex(app.metric[0].value, r"^\d+\.\d%$")
        self.assertIn(app.metric[1].value, {"Likely to churn", "Likely to stay"})


if __name__ == "__main__":
    unittest.main()
