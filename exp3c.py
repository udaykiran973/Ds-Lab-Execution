import pandas as pd
import numpy as np
data=pd.DataFrame(np.random.randn(100,3))
outliers=(data>3)|(data<-3)
print(outliers.sum())