import sys
import logging
from analytics import Research, Analytics
import config

# Настройка логирования для основного скрипта
logging.basicConfig(
    level=logging.DEBUG,
    format=config.LOG_FORMAT,
    datefmt=config.LOG_DATE_FORMAT,
    filename=config.LOG_FILE,
    filemode='a'
)

def generate_report(data, predictions):
    """Генерирует отчет на основе данных и предсказаний"""
    logging.debug("Generating report")
    
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
    
    logging.debug("Report generated successfully")
    return report

def main():
    try:
        logging.info("Starting report generation process")
        
        if len(sys.argv) != 2:
            raise ValueError("Error: Need one argument - file path")
        
        file_path = sys.argv[1]
        logging.debug(f"Processing file: {file_path}")
        
        # Чтение данных
        research = Research(file_path)
        data = research.file_reader()
        logging.info(f"Data loaded successfully: {len(data)} observations")
        
        # Создание аналитики
        analytics = Analytics(data)
        
        # Генерация предсказаний
        predictions = analytics.predict_random(config.num_of_steps)
        logging.info(f"Generated {len(predictions)} predictions")
        
        # Генерация отчета
        report = generate_report(data, predictions)
        logging.debug("Report content generated")
        
        # Сохранение отчета в файл
        analytics.save_file(report, "report", "txt")
        
        # Отправка успешного сообщения в Telegram
        research.send_telegram_message(success=True)
        
        print("\n📝 Report:")
        print(report)
        logging.info("Report generation completed successfully")
        
        return 0
        
    except Exception as e:
        logging.error(f"Report generation failed: {e}")
        
        # Отправка сообщения об ошибке в Telegram
        try:
            research = Research("")  # Создаем временный объект для отправки сообщения
            research.send_telegram_message(success=False)
        except:
            pass  # Если не удалось отправить сообщение об ошибке
        
        print(f"❌ Error: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())