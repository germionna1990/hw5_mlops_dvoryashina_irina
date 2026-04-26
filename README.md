# ML Pipeline with DVC, MLflow and Feast (Iris Dataset)

##  Цель проекта
Цель проекта — построить воспроизводимый ML-пайплайн для обучения модели на датасете Iris с использованием инструментов MLOps:
- DVC для управления данными и пайплайном
- MLflow для логирования экспериментов
- Feast для хранения признаков (Feature Store)


##  Как запустить

```bash
git clone https://github.com/germionna1990/hw5_mlops_dvoryashina_irina.git
cd hw5_mlops_dvoryashina_irina

pip install -r requirements.txt

dvc pull
dvc repro

mlflow ui
