from finstmt.forecast.config import ForecastItemConfig
from finstmt.items.config import ItemConfig

# TODO [#12]: Better matching of financial statement item names - Income Statement
#
# Would be better to use regex instead of names list. Need to first add that infrastructure,
# then apply it to the Income Statement config.

# Note that each possible extract_name must be unique, it cannot be included in multiple lists
# Also note that all incoming names will be converted to lower case and stripped of punctuation,
# then split on _ and joined with space before matching these names
INCOME_STATEMENT_INPUT_ITEMS = [
    ItemConfig(
        "revenue",
        "Revenue",
        extract_names=[
        ],
    ),
    ItemConfig(
        "cogs",
        "Cost of Goods Sold",
        extract_names=[
            ],
        forecast_config=ForecastItemConfig(pct_of="revenue"),
    ),
    ItemConfig(
        "gross_profit",
        "Gross Profit",
        force_positive=False,
        expr_str="revenue[t] - cogs[t]",
        forecast_config=ForecastItemConfig(
            make_forecast=False,
        ),
        display_verbosity=2,
    ),
    ItemConfig(
        "sga",
        "SG&A Expense",
        extract_names=[
        ],
    ),
    ItemConfig(
        "int_exp",
        "Interest Expense",
        extract_names=[
        ],
        forecast_config=ForecastItemConfig(pct_of="total_debt"),
    ),
    ItemConfig(
        "tax_exp",
        "Income Tax Expense",
        extract_names=[
        ],
        # TODO [#51]: better handling for income tax expense sign
        #
        # This item can be reported as a negative for a positive expense, so previously
        # had it as forcing positive. But also there can truly be negative expenses if
        # EBT is negative. Handle determination of whether should be forced positive
        # based on the EBT value.
        force_positive=False,
        forecast_config=ForecastItemConfig(pct_of="ebt"),
    ),
    ItemConfig(
        "rd_exp",
        "R&D Expense",
        extract_names=[
        ],
    ),
    ItemConfig(
        "dep_exp",
        "Depreciation & Amortization Expense",
        extract_names=[
        ],
    ),
    ItemConfig(
        "other_op_exp",
        "Other Operating Expenses",
        extract_names=[
        ],
    ),
    ItemConfig(
        "gain_on_sale_invest",
        "Gain on Sale of Investments",
        extract_names=[
        ],
        force_positive=False,
    ),
    ItemConfig(
        "gain_on_sale_asset",
        "Gain on Sale of Assets",
        extract_names=[
        ],
        force_positive=False,
    ),
    ItemConfig(
        "impairment",
        "Impairment Expense",
        extract_names=[
        ],
    ),
    ItemConfig(
        "op_exp",
        "Operating Expense",
        extract_names=[
        ],
        forecast_config=ForecastItemConfig(make_forecast=False),
        expr_str="rd_exp[t] + dep_exp[t] + sga[t] + other_op_exp[t]",
    ),
    ItemConfig(
        "ebit",
        "Earnings Before Interest and Taxes",
        extract_names=[
        ],
        force_positive=False,
        forecast_config=ForecastItemConfig(make_forecast=False),
        expr_str="gross_profit[t] - op_exp[t]",
    ),
    ItemConfig(
        "ebt",
        "Earnings Before Tax",
        extract_names=[
        ],
        force_positive=False,
        forecast_config=ForecastItemConfig(make_forecast=False),
        expr_str="ebit[t] - int_exp[t]",
    ),
    ItemConfig(
        "net_income",
        "Net Income",
        extract_names=[
        ],
        force_positive=False,
        forecast_config=ForecastItemConfig(make_forecast=False),
        expr_str="ebt[t] - tax_exp[t]",
    ),
]
