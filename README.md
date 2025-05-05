# GridWorld Q-Learning & Naive Bayes Classifier

Bu projede iki ana bölüm bulunmaktadır:

1. **4x4 GridWorld için Q-Learning ajanı**
2. **Naive Bayes sınıflandırıcı (sıfırdan)**

## Klasör Yapısı

```
gridworld/
    environment.py      # GridWorld ortamı
    qlearning_agent.py  # Q-Learning algoritması
    run_experiment.py   # Deneysel çalışma

naive_bayes/
    naive_bayes.py      # Naive Bayes algoritması
    dataset.py          # Örnek veri seti
    run_experiment.py   # Deneysel çalışma
```

## Çalıştırma

GridWorld Q-Learning için:
```
cd gridworld
python run_experiment.py
```

Naive Bayes için:
```
cd naive_bayes
python run_experiment.py
```

## Notlar
- Ana algoritmalar sıfırdan yazılmıştır, hazır kütüphane kullanılmamıştır.
- Kodlar modüler ve açıklamalıdır. 
