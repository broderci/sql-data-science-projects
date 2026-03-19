# Параметры для предсказаний
num_of_steps = 3

# Шаблон отчета
report_template = """Report

We made {total_observations} observations by tossing a coin: {tails} were tails and {heads} were heads.
The probabilities are {tails_pct:.2f}% and {heads_pct:.2f}%, respectively.
Our forecast is that the next {num_predictions} observations will be: {tail_predictions} tail and {head_predictions} heads."""