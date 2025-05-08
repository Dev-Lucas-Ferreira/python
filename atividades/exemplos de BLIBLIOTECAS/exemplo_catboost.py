from catboost import CatBoostClassifier
from sklearn.model_selection import train_test_split

# Dados simples (idade e gênero influenciam na preferência)
X = [[25, 0], [30, 1], [22, 0], [35, 1]]  # idade, gênero (0 = feminino, 1 = masculino)
y = [1, 0, 1, 0]  # 1 = gostou do filme, 0 = não gostou

# Separar em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)

# Modelo
model = CatBoostClassifier(verbose=0)
model.fit(X_train, y_train)

# Prever
print("Previsão:", model.predict(X_test))
