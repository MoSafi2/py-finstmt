import os
import unittest
from typing import Sequence, Dict, Optional

import pandas as pd

from finstmt import FinancialStatements
from finstmt.exc import MismatchingDatesException
from tests.conftest import DEVELOPMENT_MODE, GENERATED_PATH
from tests.expectdata.forecast.fcst_capiq_cat_annual import FCST_CAPIQ_CAT_A_INDEX_DATA_DICT
from tests.expectdata.forecast.fcst_capiq_cat_quarterly import FCST_CAPIQ_CAT_Q_INDEX_DATA_DICT
from tests.expectdata.forecast.fcst_stockrow_cat_annual import STOCKROW_FCST_CAT_A_INDEX_DATA_DICT
from tests.expectdata.forecast.fcst_stockrow_cat_annual_no_balance import FCST_STOCKROW_CAT_NO_BALANCE_A_INDEX_DATA_DICT
from tests.expectdata.forecast.fcst_stockrow_cat_quarterly import STOCKROW_FCST_CAT_Q_INDEX_DATA_DICT
from tests.expectdata.forecast.fcst_stockrow_mar_annual import FCST_STOCKROW_MAR_A_INDEX_DATA_DICT
from tests.expectdata.forecast.fcst_stockrow_mar_quarterly import FCST_STOCKROW_MAR_Q_INDEX_DATA_DICT
from tests.test_load import LoadTest

FORECAST_KWARGS = dict(
    periods=2
)


def adjust_forecast_methods(stmts: FinancialStatements, adjust_dict: Dict[str, Sequence[str]]):
    for method, var_list in adjust_dict.items():
        for var in var_list:
            stmts.config.update(var, ['forecast_config', 'method'], method)


class ForecastTest(LoadTest):
    a_adjust_dict: Dict[str, Sequence[str]]
    q_adjust_dict: Dict[str, Sequence[str]]

    def test_annual(self, stmts: FinancialStatements, data: Optional[Dict[str, pd.Series]] = None, **kwargs):
        fcst_kwargs = FORECAST_KWARGS.copy()
        fcst_kwargs.update(kwargs)
        adjust_forecast_methods(stmts, self.a_adjust_dict)
        fcst = stmts.forecast(**fcst_kwargs)
        if DEVELOPMENT_MODE:
            fig = fcst.plot()
            out_path = os.path.join(GENERATED_PATH, f'{self.name}_annual.pdf')
            fig.savefig(out_path)
        super().test_annual(fcst, data=data)

    def test_quarterly(self, stmts: FinancialStatements, data: Optional[Dict[str, pd.Series]] = None, **kwargs):
        fcst_kwargs = FORECAST_KWARGS.copy()
        fcst_kwargs.update(kwargs)
        adjust_forecast_methods(stmts, self.q_adjust_dict)
        fcst = stmts.forecast(**fcst_kwargs)
        if DEVELOPMENT_MODE:
            fig = fcst.plot()
            out_path = os.path.join(GENERATED_PATH, f'{self.name}_quarterly.pdf')
            fig.savefig(out_path)
        super().test_quarterly(fcst, data=data)


class TestForecastStockrowCAT(ForecastTest):
    name = 'fcst_stockrow_cat'
    q_test_data_dict = STOCKROW_FCST_CAT_Q_INDEX_DATA_DICT
    a_test_data_dict = STOCKROW_FCST_CAT_A_INDEX_DATA_DICT
    a_adjust_dict = q_adjust_dict = dict(
        trend=[
            'cogs',
            'cash',
            'inventory',
            'payables',
            'retained_earnings',
        ],
        auto=[
            'rd_exp',
        ],
        recent=[
            'lt_invest',
        ],
        mean=[
            # Because zeroes
            'dep_exp',
            'other_op_exp',
            'gain_on_sale_invest',
            'gain_on_sale_asset',
            'impairment',
            'st_invest',
            'def_tax_st',
            'other_current_assets',
            'gross_ppe',
            'dep',
            'other_lt_assets',
            'current_lt_debt',
            'tax_liab_lt',
            'tax_liab_st',
            'other_current_liab',
            'deferred_rev',
            'other_lt_liab',
            'common_stock',
            'minority_interest',

            # Because flat
            'int_exp',
            'tax_exp',
            'receivables',
            'goodwill',
            'deposit_liab',
        ]
    )

    def test_annual(self, annual_stockrow_stmts_cat: FinancialStatements):
        super().test_annual(annual_stockrow_stmts_cat)

    def test_annual_no_balance(self, annual_stockrow_stmts_cat: FinancialStatements):
        super().test_annual(
            annual_stockrow_stmts_cat, data=FCST_STOCKROW_CAT_NO_BALANCE_A_INDEX_DATA_DICT, balance=False
        )

    def test_quarterly(self, quarterly_stockrow_stmts_cat: FinancialStatements):
        super().test_quarterly(quarterly_stockrow_stmts_cat)


class TestForecastStockrowMAR(ForecastTest):
    name = 'fcst_stockrow_mar'
    q_test_data_dict = FCST_STOCKROW_MAR_Q_INDEX_DATA_DICT
    a_test_data_dict = FCST_STOCKROW_MAR_A_INDEX_DATA_DICT
    a_adjust_dict = q_adjust_dict = dict(
        trend=[
            'revenue',
            'sga',
            'cogs',
            'cash',
            'payables',
        ],
        auto=[

        ],
        recent=[
            'lt_invest',
            'inventory',
            'goodwill',
            'other_lt_assets',
            'deferred_rev',
            'tax_liab_lt',
        ],
        mean=[
            # Because zeroes
            'rd_exp',
            'dep_exp',
            'other_op_exp',
            'gain_on_sale_invest',
            'gain_on_sale_asset',
            'impairment',
            'st_invest',
            'def_tax_st',
            'other_current_assets',
            'gross_ppe',
            'dep',
            'current_lt_debt',
            'tax_liab_st',
            'common_stock',
            'minority_interest',

            # Because flat
            'int_exp',
            'tax_exp',
            'deposit_liab',
        ]
    )

    def test_annual(self, annual_stockrow_stmts_mar: FinancialStatements):
        super().test_annual(annual_stockrow_stmts_mar)

    def test_quarterly(self, quarterly_stockrow_stmts_mar: FinancialStatements):
        super().test_quarterly(quarterly_stockrow_stmts_mar)


class TestForecastCapitalIQCAT(ForecastTest):
    name = 'fcst_capiq_cat'
    q_test_data_dict = FCST_CAPIQ_CAT_Q_INDEX_DATA_DICT
    a_test_data_dict = FCST_CAPIQ_CAT_A_INDEX_DATA_DICT
    a_adjust_dict = q_adjust_dict = dict(
        trend=[
            'cogs',
            'cash',
            'inventory',
            'payables',
            'common_stock',
            'other_income',
            'retained_earnings',
        ],
        auto=[
            'rd_exp',
        ],
        recent=[
            'lt_invest',
        ],
        mean=[
            # Because zeroes
            'dep_exp',
            'other_op_exp',
            'gain_on_sale_invest',
            'gain_on_sale_asset',
            'impairment',
            'st_invest',
            'def_tax_st',
            'other_current_assets',
            'gross_ppe',
            'dep',
            'other_lt_assets',
            'current_lt_debt',
            'tax_liab_lt',
            'tax_liab_st',
            'other_current_liab',
            'deferred_rev',
            'other_lt_liab',
            'minority_interest',

            # Because flat
            'int_exp',
            'tax_exp',
            'receivables',
            'goodwill',
            'deposit_liab',
        ]
    )

    def test_annual(self, annual_capiq_stmts: FinancialStatements):
        super().test_annual(annual_capiq_stmts)

    def test_quarterly(self, quarterly_capiq_stmts: FinancialStatements):
        super().test_quarterly(quarterly_capiq_stmts)
