import sys
from analytics import Research, Analytics
import config

def generate_report(data, predictions):
    """Генерирует отчет на основе данных и предсказаний"""
    
    # Подсчеты для реальных данных
    calculator = Research.Calculations()
    heads, tails = calculator.counts(data)
    heads_pct, tails_pct = calculator.fractions(heads, tails)
    
    # Подсчеты для предсказаний
    pred_heads = sum(1 for p in predictions if p[0] == 1)
    pred_tails = sum(1 for p in predictions if p[1] == 1)
    
    # Заполнение шаблона
    report = config.report_template.format(
        total_observations=len(data),
        tails=tails,
        heads=heads,
        tails_pct=tails_pct * 100,
        heads_pct=heads_pct * 100,
        num_predictions=len(predictions),
        tail_predictions=pred_tails,
        head_predictions=pred_heads
    )
    
    return report

def main():
    try:
        if len(sys.argv) != 2:
            raise ValueError("Error: Need one argument - file path")
        
        file_path = sys.argv[1]
        
        # Чтение данных
        research = Research(file_path)
        data = research.file_reader()
        
        # Создание аналитики
        analytics = Analytics(data)
        
        # Генерация предсказаний
        predictions = analytics.predict_random(config.num_of_steps)
        
        # Генерация отчета
        report = generate_report(data, predictions)
        print(report)
        
        # Сохранение отчета в файл
        analytics.save_file(report, "report", "txt")
        
        return 0
        
    except Exception as e:
        print(f" Error: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())