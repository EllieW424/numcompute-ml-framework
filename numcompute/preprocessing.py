import numpy as np

class StandardScaler:

    def __init__(self):
        self.mean_ = None
        self.std_ = None
        
    def fit(self, X):
        X = np.asarray(X, dtype=float)
        self.mean_ = np.mean(X, axis=0)
        self.std_ = np.std(X, axis=0)
        # 防止除以 0
        self.std_[self.std_ == 0] = 1.0
        return self
        
    def transform(self, X):
        X = np. asarray(X, dtype=float)
        return (X - self.mean_) / self.std_
        
    def fit_transform(self, X):
        return self.fit(X).transform(X)


class MinMaxScaler:
    
    def _init__(self):
        self.min_ = None
        self.max_ = None
        
    def fit (self, X):
        self.min_ = np.min(X, axis=0)
        self.max_ = np.max(X, axis=0)
        
    def transform(self, X):
        return (X - self.min_) / (self.max_ - self.min_)
    
    def fit_transform(self, X):
        return self.fit(X). transform(X)
    
    def inverse_transform(self, X):
        return (X * self.max_ - self.min_) + self.min_
        
class OneHotEncoder:
    def __init__(self):
        self._values = []
        self._number = []
        self._ids = []
        
    def fit(self, X):
        if len(X.shape) != 2:
            raise ValueError("X must be 2-dimension")
        for col_idx in range(X.shape[1]):
            col = X[:, col_idx]
            unique_values = np.unique(col)
            self._values.append(unique_values)
            self._number.append(len(unique_values))
            self._ids.append({v: i for i, v in enumerate(unique_values)})
        return self
        
    def transform(self, X):
        if len(X.shape) != 2 and X.shape[1] == len(self._number):
            raise ValueError(f"X must be 2-dimension and number of columns must be {len(self._number)}")
        X_transformed = []
        for col_idx in range(X.shape[1]):
            col = X[:, col_idx]
            n_cls = self._number[col_idx]
            v_id = np.array([ self._ids[col_idx].get(value, -1) for value in col ])
            eye = np.concatenate((np.zeros((1, n_cls)), np.eye(n_cls)))
            X_transformed.append(eye[v_id + 1])
        X_transformed = np.concatenate(X_transformed, axis=1)
        return X_transformed
    
    def fit_transform (self, X):
        return self.fit(X). transform(X)
    
    def inverse_transform(self, X):
        if len(X.shape) != 2:
            raise ValueError("X must be 2-dimension")
        col_range = np.cumsum(self._number)
        X_transformed = []

        col_idx = 0
        start = 0
        for end in col_range:
            oh_encs = X[:, start:end]
            oh_encs = np.concatenate((np.zeros((oh_encs.shape[0], 1)), oh_encs), axis=1)
            unique_values = np.append(self._values[col_idx], 'UNKNOWN')
            X_transformed.append(unique_values[oh_encs.argmax(axis=1) - 1].reshape(-1, 1))
            start = end
            col_idx = col_idx + 1
            
        X_transformed = np.concatenate(X_transformed, axis=1)
        return X_transformed