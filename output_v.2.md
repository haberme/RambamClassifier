# Train

## No overlap

### SVC train - no overlap:

Best parameters for SVC are: {'clf__C': 10, 'clf__kernel': 'linear', 'vect__ngram_range': (1, 2), 'vect__use_idf': True}

| i | params | mean train score | std train score | mean test score | std test score | rank test score |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| 1 | {'clf__C': 10, 'clf__kernel': 'linear', 'vect__ngram_range': (1, 1), 'vect__use_idf': True} | 0.9999200294302772 | 3.9985984144090587e-05 | 0.9715177214177134 | 0.003924605512662106 | 2 |
| 2 | {'clf__C': 10, 'clf__kernel': 'linear', 'vect__ngram_range': (1, 1), 'vect__use_idf': False} | 0.9998799150680382 | 4.0339348330025056e-05 | 0.9569565565245219 | 0.005344887599447622 | 7 |
| 3 | {'clf__C': 10, 'clf__kernel': 'linear', 'vect__ngram_range': (1, 2), 'vect__use_idf': True} | 0.9999200294302772 | 3.9985984144090587e-05 | 0.9716777342187375 | 0.0035550277703157904 | 1 |
| 4 | {'clf__C': 10, 'clf__kernel': 'linear', 'vect__ngram_range': (1, 2), 'vect__use_idf': False} | 0.9998800332699245 | 3.9807731637179884e-05 | 0.959116729338347 | 0.005371803502361702 | 5 |
| 5 | {'clf__C': 10, 'clf__kernel': 'poly', 'vect__ngram_range': (1, 1), 'vect__use_idf': True} | 0.04664392347969153 | 7.976292093331756e-05 | 0.04664373149851988 | 0.00031783947365221374 | 9 |
| 6 | {'clf__C': 10, 'clf__kernel': 'poly', 'vect__ngram_range': (1, 1), 'vect__use_idf': False} | 0.04664392347969153 | 7.976292093331756e-05 | 0.04664373149851988 | 0.00031783947365221374 | 9 |
| 7 | {'clf__C': 10, 'clf__kernel': 'poly', 'vect__ngram_range': (1, 2), 'vect__use_idf': True} | 0.04664392347969153 | 7.976292093331756e-05 | 0.04664373149851988 | 0.00031783947365221374 | 9 |
| 8 | {'clf__C': 10, 'clf__kernel': 'poly', 'vect__ngram_range': (1, 2), 'vect__use_idf': False} | 0.04664392347969153 | 7.976292093331756e-05 | 0.04664373149851988 | 0.00031783947365221374 | 9 |
| 9 | {'clf__C': 10, 'clf__kernel': 'rbf', 'vect__ngram_range': (1, 1), 'vect__use_idf': True} | 0.04664392347969153 | 7.976292093331756e-05 | 0.04664373149851988 | 0.00031783947365221374 | 9 |
| 10 | {'clf__C': 10, 'clf__kernel': 'rbf', 'vect__ngram_range': (1, 1), 'vect__use_idf': False} | 0.04664392347969153 | 7.976292093331756e-05 | 0.04664373149851988 | 0.00031783947365221374 | 9 |
| 11 | {'clf__C': 10, 'clf__kernel': 'rbf', 'vect__ngram_range': (1, 2), 'vect__use_idf': True} | 0.04664392347969153 | 7.976292093331756e-05 | 0.04664373149851988 | 0.00031783947365221374 | 9 |
| 12 | {'clf__C': 10, 'clf__kernel': 'rbf', 'vect__ngram_range': (1, 2), 'vect__use_idf': False} | 0.04664392347969153 | 7.976292093331756e-05 | 0.04664373149851988 | 0.00031783947365221374 | 9 |
| 13 | {'clf__C': 10, 'clf__kernel': 'sigmoid', 'vect__ngram_range': (1, 1), 'vect__use_idf': True} | 0.04664392347969153 | 7.976292093331756e-05 | 0.04664373149851988 | 0.00031783947365221374 | 9 |
| 14 | {'clf__C': 10, 'clf__kernel': 'sigmoid', 'vect__ngram_range': (1, 1), 'vect__use_idf': False} | 0.04664392347969153 | 7.976292093331756e-05 | 0.04664373149851988 | 0.00031783947365221374 | 9 |
| 15 | {'clf__C': 10, 'clf__kernel': 'sigmoid', 'vect__ngram_range': (1, 2), 'vect__use_idf': True} | 0.04664392347969153 | 7.976292093331756e-05 | 0.04664373149851988 | 0.00031783947365221374 | 9 |
| 16 | {'clf__C': 10, 'clf__kernel': 'sigmoid', 'vect__ngram_range': (1, 2), 'vect__use_idf': False} | 0.04664392347969153 | 7.976292093331756e-05 | 0.04664373149851988 | 0.00031783947365221374 | 9 |
| 17 | {'clf__C': 100, 'clf__kernel': 'linear', 'vect__ngram_range': (1, 1), 'vect__use_idf': True} | 1.0 | 0.0 | 0.9699175934074726 | 0.004358944617969149 | 4 |
| 18 | {'clf__C': 100, 'clf__kernel': 'linear', 'vect__ngram_range': (1, 1), 'vect__use_idf': False} | 1.0 | 0.0 | 0.9565565245219617 | 0.00540837581239375 | 8 |
| 19 | {'clf__C': 100, 'clf__kernel': 'linear', 'vect__ngram_range': (1, 2), 'vect__use_idf': True} | 1.0 | 0.0 | 0.9703176254100329 | 0.004162645375342439 | 3 |
| 20 | {'clf__C': 100, 'clf__kernel': 'linear', 'vect__ngram_range': (1, 2), 'vect__use_idf': False} | 1.0 | 0.0 | 0.9585566845347627 | 0.0056797503585056955 | 6 |
| 21 | {'clf__C': 100, 'clf__kernel': 'poly', 'vect__ngram_range': (1, 1), 'vect__use_idf': True} | 0.04664392347969153 | 7.976292093331756e-05 | 0.04664373149851988 | 0.00031783947365221374 | 9 |
| 22 | {'clf__C': 100, 'clf__kernel': 'poly', 'vect__ngram_range': (1, 1), 'vect__use_idf': False} | 0.04664392347969153 | 7.976292093331756e-05 | 0.04664373149851988 | 0.00031783947365221374 | 9 |
| 23 | {'clf__C': 100, 'clf__kernel': 'poly', 'vect__ngram_range': (1, 2), 'vect__use_idf': True} | 0.04664392347969153 | 7.976292093331756e-05 | 0.04664373149851988 | 0.00031783947365221374 | 9 |
| 24 | {'clf__C': 100, 'clf__kernel': 'poly', 'vect__ngram_range': (1, 2), 'vect__use_idf': False} | 0.04664392347969153 | 7.976292093331756e-05 | 0.04664373149851988 | 0.00031783947365221374 | 9 |
| 25 | {'clf__C': 100, 'clf__kernel': 'rbf', 'vect__ngram_range': (1, 1), 'vect__use_idf': True} | 0.04664392347969153 | 7.976292093331756e-05 | 0.04664373149851988 | 0.00031783947365221374 | 9 |
| 26 | {'clf__C': 100, 'clf__kernel': 'rbf', 'vect__ngram_range': (1, 1), 'vect__use_idf': False} | 0.04664392347969153 | 7.976292093331756e-05 | 0.04664373149851988 | 0.00031783947365221374 | 9 |
| 27 | {'clf__C': 100, 'clf__kernel': 'rbf', 'vect__ngram_range': (1, 2), 'vect__use_idf': True} | 0.04664392347969153 | 7.976292093331756e-05 | 0.04664373149851988 | 0.00031783947365221374 | 9 |
| 28 | {'clf__C': 100, 'clf__kernel': 'rbf', 'vect__ngram_range': (1, 2), 'vect__use_idf': False} | 0.04664392347969153 | 7.976292093331756e-05 | 0.04664373149851988 | 0.00031783947365221374 | 9 |
| 29 | {'clf__C': 100, 'clf__kernel': 'sigmoid', 'vect__ngram_range': (1, 1), 'vect__use_idf': True} | 0.04664392347969153 | 7.976292093331756e-05 | 0.04664373149851988 | 0.00031783947365221374 | 9 |
| 30 | {'clf__C': 100, 'clf__kernel': 'sigmoid', 'vect__ngram_range': (1, 1), 'vect__use_idf': False} | 0.04664392347969153 | 7.976292093331756e-05 | 0.04664373149851988 | 0.00031783947365221374 | 9 |
| 31 | {'clf__C': 100, 'clf__kernel': 'sigmoid', 'vect__ngram_range': (1, 2), 'vect__use_idf': True} | 0.04664392347969153 | 7.976292093331756e-05 | 0.04664373149851988 | 0.00031783947365221374 | 9 |
| 32 | {'clf__C': 100, 'clf__kernel': 'sigmoid', 'vect__ngram_range': (1, 2), 'vect__use_idf': False} | 0.04664392347969153 | 7.976292093331756e-05 | 0.04664373149851988 | 0.00031783947365221374 | 9 |



### LinearSVC train - no overlap:

Best parameters for LinearSVC are: {'clf__C': 10, 'clf__loss': 'hinge', 'vect__ngram_range': (1, 2), 'vect__use_idf': True}

| i | params | mean train score | std train score | mean test score | std test score | rank test score |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| 1 | {'clf__C': 10, 'clf__loss': 'hinge', 'vect__ngram_range': (1, 1), 'vect__use_idf': True} | 0.9999200294302772 | 3.9985984144090587e-05 | 0.9775982078566285 | 0.0025582506640612363 | 8 |
| 2 | {'clf__C': 10, 'clf__loss': 'hinge', 'vect__ngram_range': (1, 1), 'vect__use_idf': False} | 0.9999200294302772 | 3.9985984144090587e-05 | 0.970637651012081 | 0.003037937487784502 | 19 |
| 3 | {'clf__C': 10, 'clf__loss': 'hinge', 'vect__ngram_range': (1, 2), 'vect__use_idf': True} | 0.9999400274304773 | 4.896796702537254e-05 | 0.9810384830786463 | 0.001508177899446953 | 1 |
| 4 | {'clf__C': 10, 'clf__loss': 'hinge', 'vect__ngram_range': (1, 2), 'vect__use_idf': False} | 0.9999000713422619 | 6.311349674014761e-05 | 0.9751180094407552 | 0.0033419856568290213 | 13 |
| 5 | {'clf__C': 10, 'clf__loss': 'squared_hinge', 'vect__ngram_range': (1, 1), 'vect__use_idf': True} | 1.0 | 0.0 | 0.9774381950556045 | 0.002486345406134442 | 9 |
| 6 | {'clf__C': 10, 'clf__loss': 'squared_hinge', 'vect__ngram_range': (1, 1), 'vect__use_idf': False} | 1.0 | 0.0 | 0.9703976318105448 | 0.003081291324448622 | 20 |
| 7 | {'clf__C': 10, 'clf__loss': 'squared_hinge', 'vect__ngram_range': (1, 2), 'vect__use_idf': True} | 1.0 | 0.0 | 0.9809584766781343 | 0.001671288215398441 | 3 |
| 8 | {'clf__C': 10, 'clf__loss': 'squared_hinge', 'vect__ngram_range': (1, 2), 'vect__use_idf': False} | 1.0 | 0.0 | 0.9747179774381951 | 0.0033744872549248102 | 16 |
| 9 | {'clf__C': 100, 'clf__loss': 'hinge', 'vect__ngram_range': (1, 1), 'vect__use_idf': True} | 1.0 | 0.0 | 0.9776782142571405 | 0.0025487641130242547 | 7 |
| 10 | {'clf__C': 100, 'clf__loss': 'hinge', 'vect__ngram_range': (1, 1), 'vect__use_idf': False} | 1.0 | 0.0 | 0.9703976318105448 | 0.003135117467521215 | 20 |
| 11 | {'clf__C': 100, 'clf__loss': 'hinge', 'vect__ngram_range': (1, 2), 'vect__use_idf': True} | 1.0 | 0.0 | 0.9810384830786463 | 0.001508177899446953 | 1 |
| 12 | {'clf__C': 100, 'clf__loss': 'hinge', 'vect__ngram_range': (1, 2), 'vect__use_idf': False} | 1.0 | 0.0 | 0.9748779902392192 | 0.0036103275533754193 | 14 |
| 13 | {'clf__C': 100, 'clf__loss': 'squared_hinge', 'vect__ngram_range': (1, 1), 'vect__use_idf': True} | 1.0 | 0.0 | 0.9769581566525322 | 0.0027204388521503407 | 10 |
| 14 | {'clf__C': 100, 'clf__loss': 'squared_hinge', 'vect__ngram_range': (1, 1), 'vect__use_idf': False} | 1.0 | 0.0 | 0.9703976318105448 | 0.003135117467521215 | 20 |
| 15 | {'clf__C': 100, 'clf__loss': 'squared_hinge', 'vect__ngram_range': (1, 2), 'vect__use_idf': True} | 1.0 | 0.0 | 0.980638451076086 | 0.0018646276830062319 | 4 |
| 16 | {'clf__C': 100, 'clf__loss': 'squared_hinge', 'vect__ngram_range': (1, 2), 'vect__use_idf': False} | 1.0 | 0.0 | 0.9748779902392192 | 0.0036103275533754193 | 14 |
| 17 | {'clf__C': 1000, 'clf__loss': 'hinge', 'vect__ngram_range': (1, 1), 'vect__use_idf': True} | 1.0 | 0.0 | 0.9767981438515081 | 0.0026743857222405187 | 11 |
| 18 | {'clf__C': 1000, 'clf__loss': 'hinge', 'vect__ngram_range': (1, 1), 'vect__use_idf': False} | 1.0 | 0.0 | 0.9700776062084967 | 0.0032010688245566847 | 24 |
| 19 | {'clf__C': 1000, 'clf__loss': 'hinge', 'vect__ngram_range': (1, 2), 'vect__use_idf': True} | 1.0 | 0.0 | 0.9801584126730138 | 0.0018630692537393288 | 6 |
| 20 | {'clf__C': 1000, 'clf__loss': 'hinge', 'vect__ngram_range': (1, 2), 'vect__use_idf': False} | 1.0 | 0.0 | 0.9745579646371709 | 0.0036252983333953043 | 18 |
| 21 | {'clf__C': 1000, 'clf__loss': 'squared_hinge', 'vect__ngram_range': (1, 1), 'vect__use_idf': True} | 1.0 | 0.0 | 0.9767981438515081 | 0.0026743857222405187 | 11 |
| 22 | {'clf__C': 1000, 'clf__loss': 'squared_hinge', 'vect__ngram_range': (1, 1), 'vect__use_idf': False} | 1.0 | 0.0 | 0.9701576126090087 | 0.0032493816930531313 | 23 |
| 23 | {'clf__C': 1000, 'clf__loss': 'squared_hinge', 'vect__ngram_range': (1, 2), 'vect__use_idf': True} | 1.0 | 0.0 | 0.9802384190735259 | 0.0019088295215848028 | 5 |
| 24 | {'clf__C': 1000, 'clf__loss': 'squared_hinge', 'vect__ngram_range': (1, 2), 'vect__use_idf': False} | 1.0 | 0.0 | 0.974637971037683 | 0.0035354342674919306 | 17 |


## With overlap

### SVC train - with overlap:

Best parameters for SVC are: {'clf__C': 10, 'clf__kernel': 'linear', 'vect__ngram_range': (1, 2), 'vect__use_idf': True}

| i | params | mean train score | std train score | mean test score | std test score | rank test score |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| 1 | {'clf__C': 10, 'clf__kernel': 'linear', 'vect__ngram_range': (1, 1), 'vect__use_idf': True} | 0.9998998731560533 | 6.34873423852666e-05 | 0.9740779262340987 | 0.0030797060435500553 | 2 |
| 2 | {'clf__C': 10, 'clf__kernel': 'linear', 'vect__ngram_range': (1, 1), 'vect__use_idf': False} | 0.999919949445955 | 4.002593004209013e-05 | 0.9579966397311785 | 0.003736174579092023 | 7 |
| 3 | {'clf__C': 10, 'clf__kernel': 'linear', 'vect__ngram_range': (1, 2), 'vect__use_idf': True} | 0.9998998731560533 | 6.34873423852666e-05 | 0.974637971037683 | 0.002325748189377554 | 1 |
| 4 | {'clf__C': 10, 'clf__kernel': 'linear', 'vect__ngram_range': (1, 2), 'vect__use_idf': False} | 0.999939947446155 | 4.903322338319769e-05 | 0.9627970237619009 | 0.004004502937894867 | 5 |
| 5 | {'clf__C': 10, 'clf__kernel': 'poly', 'vect__ngram_range': (1, 1), 'vect__use_idf': True} | 0.04664392347969153 | 7.976292093331756e-05 | 0.04664373149851988 | 0.00031783947365221374 | 9 |
| 6 | {'clf__C': 10, 'clf__kernel': 'poly', 'vect__ngram_range': (1, 1), 'vect__use_idf': False} | 0.04664392347969153 | 7.976292093331756e-05 | 0.04664373149851988 | 0.00031783947365221374 | 9 |
| 7 | {'clf__C': 10, 'clf__kernel': 'poly', 'vect__ngram_range': (1, 2), 'vect__use_idf': True} | 0.04664392347969153 | 7.976292093331756e-05 | 0.04664373149851988 | 0.00031783947365221374 | 9 |
| 8 | {'clf__C': 10, 'clf__kernel': 'poly', 'vect__ngram_range': (1, 2), 'vect__use_idf': False} | 0.04664392347969153 | 7.976292093331756e-05 | 0.04664373149851988 | 0.00031783947365221374 | 9 |
| 9 | {'clf__C': 10, 'clf__kernel': 'rbf', 'vect__ngram_range': (1, 1), 'vect__use_idf': True} | 0.04664392347969153 | 7.976292093331756e-05 | 0.04664373149851988 | 0.00031783947365221374 | 9 |
| 10 | {'clf__C': 10, 'clf__kernel': 'rbf', 'vect__ngram_range': (1, 1), 'vect__use_idf': False} | 0.04664392347969153 | 7.976292093331756e-05 | 0.04664373149851988 | 0.00031783947365221374 | 9 |
| 11 | {'clf__C': 10, 'clf__kernel': 'rbf', 'vect__ngram_range': (1, 2), 'vect__use_idf': True} | 0.04664392347969153 | 7.976292093331756e-05 | 0.04664373149851988 | 0.00031783947365221374 | 9 |
| 12 | {'clf__C': 10, 'clf__kernel': 'rbf', 'vect__ngram_range': (1, 2), 'vect__use_idf': False} | 0.04664392347969153 | 7.976292093331756e-05 | 0.04664373149851988 | 0.00031783947365221374 | 9 |
| 13 | {'clf__C': 10, 'clf__kernel': 'sigmoid', 'vect__ngram_range': (1, 1), 'vect__use_idf': True} | 0.04664392347969153 | 7.976292093331756e-05 | 0.04664373149851988 | 0.00031783947365221374 | 9 |
| 14 | {'clf__C': 10, 'clf__kernel': 'sigmoid', 'vect__ngram_range': (1, 1), 'vect__use_idf': False} | 0.04664392347969153 | 7.976292093331756e-05 | 0.04664373149851988 | 0.00031783947365221374 | 9 |
| 15 | {'clf__C': 10, 'clf__kernel': 'sigmoid', 'vect__ngram_range': (1, 2), 'vect__use_idf': True} | 0.04664392347969153 | 7.976292093331756e-05 | 0.04664373149851988 | 0.00031783947365221374 | 9 |
| 16 | {'clf__C': 10, 'clf__kernel': 'sigmoid', 'vect__ngram_range': (1, 2), 'vect__use_idf': False} | 0.04664392347969153 | 7.976292093331756e-05 | 0.04664373149851988 | 0.00031783947365221374 | 9 |
| 17 | {'clf__C': 100, 'clf__kernel': 'linear', 'vect__ngram_range': (1, 1), 'vect__use_idf': True} | 0.9999799237100984 | 4.015257980323206e-05 | 0.9735178814305144 | 0.0031595197150360165 | 3 |
| 18 | {'clf__C': 100, 'clf__kernel': 'linear', 'vect__ngram_range': (1, 1), 'vect__use_idf': False} | 0.9999799237100984 | 4.015257980323206e-05 | 0.9575966077286183 | 0.0038611236470086643 | 8 |
| 19 | {'clf__C': 100, 'clf__kernel': 'linear', 'vect__ngram_range': (1, 2), 'vect__use_idf': True} | 0.9999799237100984 | 4.015257980323206e-05 | 0.9731978558284663 | 0.0028122479545567036 | 4 |
| 20 | {'clf__C': 100, 'clf__kernel': 'linear', 'vect__ngram_range': (1, 2), 'vect__use_idf': False} | 0.9999799237100984 | 4.015257980323206e-05 | 0.9620769661572925 | 0.0039802968262012154 | 6 |
| 21 | {'clf__C': 100, 'clf__kernel': 'poly', 'vect__ngram_range': (1, 1), 'vect__use_idf': True} | 0.04664392347969153 | 7.976292093331756e-05 | 0.04664373149851988 | 0.00031783947365221374 | 9 |
| 22 | {'clf__C': 100, 'clf__kernel': 'poly', 'vect__ngram_range': (1, 1), 'vect__use_idf': False} | 0.04664392347969153 | 7.976292093331756e-05 | 0.04664373149851988 | 0.00031783947365221374 | 9 |
| 23 | {'clf__C': 100, 'clf__kernel': 'poly', 'vect__ngram_range': (1, 2), 'vect__use_idf': True} | 0.04664392347969153 | 7.976292093331756e-05 | 0.04664373149851988 | 0.00031783947365221374 | 9 |
| 24 | {'clf__C': 100, 'clf__kernel': 'poly', 'vect__ngram_range': (1, 2), 'vect__use_idf': False} | 0.04664392347969153 | 7.976292093331756e-05 | 0.04664373149851988 | 0.00031783947365221374 | 9 |
| 25 | {'clf__C': 100, 'clf__kernel': 'rbf', 'vect__ngram_range': (1, 1), 'vect__use_idf': True} | 0.04664392347969153 | 7.976292093331756e-05 | 0.04664373149851988 | 0.00031783947365221374 | 9 |
| 26 | {'clf__C': 100, 'clf__kernel': 'rbf', 'vect__ngram_range': (1, 1), 'vect__use_idf': False} | 0.04664392347969153 | 7.976292093331756e-05 | 0.04664373149851988 | 0.00031783947365221374 | 9 |
| 27 | {'clf__C': 100, 'clf__kernel': 'rbf', 'vect__ngram_range': (1, 2), 'vect__use_idf': True} | 0.04664392347969153 | 7.976292093331756e-05 | 0.04664373149851988 | 0.00031783947365221374 | 9 |
| 28 | {'clf__C': 100, 'clf__kernel': 'rbf', 'vect__ngram_range': (1, 2), 'vect__use_idf': False} | 0.04664392347969153 | 7.976292093331756e-05 | 0.04664373149851988 | 0.00031783947365221374 | 9 |
| 29 | {'clf__C': 100, 'clf__kernel': 'sigmoid', 'vect__ngram_range': (1, 1), 'vect__use_idf': True} | 0.04664392347969153 | 7.976292093331756e-05 | 0.04664373149851988 | 0.00031783947365221374 | 9 |
| 30 | {'clf__C': 100, 'clf__kernel': 'sigmoid', 'vect__ngram_range': (1, 1), 'vect__use_idf': False} | 0.04664392347969153 | 7.976292093331756e-05 | 0.04664373149851988 | 0.00031783947365221374 | 9 |
| 31 | {'clf__C': 100, 'clf__kernel': 'sigmoid', 'vect__ngram_range': (1, 2), 'vect__use_idf': True} | 0.04664392347969153 | 7.976292093331756e-05 | 0.04664373149851988 | 0.00031783947365221374 | 9 |
| 32 | {'clf__C': 100, 'clf__kernel': 'sigmoid', 'vect__ngram_range': (1, 2), 'vect__use_idf': False} | 0.04664392347969153 | 7.976292093331756e-05 | 0.04664373149851988 | 0.00031783947365221374 | 9 |



### LinearSVC train - with overlap:

Best parameters for LinearSVC are: {'clf__C': 10, 'clf__loss': 'hinge', 'vect__ngram_range': (1, 2), 'vect__use_idf': True}

| i | params | mean train score | std train score | mean test score | std test score | rank test score |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| 1 | {'clf__C': 10, 'clf__loss': 'hinge', 'vect__ngram_range': (1, 1), 'vect__use_idf': True} | 0.9998998731560533 | 6.34873423852666e-05 | 0.9799183934714777 | 0.0007822731537510058 | 7 |
| 2 | {'clf__C': 10, 'clf__loss': 'hinge', 'vect__ngram_range': (1, 1), 'vect__use_idf': False} | 0.9998998731560533 | 6.34873423852666e-05 | 0.9724777982238579 | 0.000577662480251788 | 19 |
| 3 | {'clf__C': 10, 'clf__loss': 'hinge', 'vect__ngram_range': (1, 2), 'vect__use_idf': True} | 0.999919949445955 | 4.002593004209013e-05 | 0.982398591887351 | 0.0014381684533930866 | 1 |
| 4 | {'clf__C': 10, 'clf__loss': 'hinge', 'vect__ngram_range': (1, 2), 'vect__use_idf': False} | 0.9998998731560533 | 6.34873423852666e-05 | 0.9771981758540683 | 0.001891708024817902 | 13 |
| 5 | {'clf__C': 10, 'clf__loss': 'squared_hinge', 'vect__ngram_range': (1, 1), 'vect__use_idf': True} | 0.9999799237100984 | 4.015257980323206e-05 | 0.9795183614689175 | 0.0012137728059298581 | 9 |
| 6 | {'clf__C': 10, 'clf__loss': 'squared_hinge', 'vect__ngram_range': (1, 1), 'vect__use_idf': False} | 0.9999799237100984 | 4.015257980323206e-05 | 0.9723977918233458 | 0.0006818666360960782 | 21 |
| 7 | {'clf__C': 10, 'clf__loss': 'squared_hinge', 'vect__ngram_range': (1, 2), 'vect__use_idf': True} | 0.9999799237100984 | 4.015257980323206e-05 | 0.9821585726858149 | 0.0013149704904676133 | 4 |
| 8 | {'clf__C': 10, 'clf__loss': 'squared_hinge', 'vect__ngram_range': (1, 2), 'vect__use_idf': False} | 0.9999799237100984 | 4.015257980323206e-05 | 0.9770381630530443 | 0.0024597853996918516 | 14 |
| 9 | {'clf__C': 100, 'clf__loss': 'hinge', 'vect__ngram_range': (1, 1), 'vect__use_idf': True} | 0.9999799237100984 | 4.015257980323206e-05 | 0.9795983678694296 | 0.0011758211078874412 | 8 |
| 10 | {'clf__C': 100, 'clf__loss': 'hinge', 'vect__ngram_range': (1, 1), 'vect__use_idf': False} | 0.9999799237100984 | 4.015257980323206e-05 | 0.9723177854228339 | 0.0005194674144511799 | 22 |
| 11 | {'clf__C': 100, 'clf__loss': 'hinge', 'vect__ngram_range': (1, 2), 'vect__use_idf': True} | 0.9999799237100984 | 4.015257980323206e-05 | 0.9823185854868389 | 0.0013950802560163916 | 2 |
| 12 | {'clf__C': 100, 'clf__loss': 'hinge', 'vect__ngram_range': (1, 2), 'vect__use_idf': False} | 0.9999799237100984 | 4.015257980323206e-05 | 0.9770381630530443 | 0.0019443094846368896 | 14 |
| 13 | {'clf__C': 100, 'clf__loss': 'squared_hinge', 'vect__ngram_range': (1, 1), 'vect__use_idf': True} | 0.9999799237100984 | 4.015257980323206e-05 | 0.9794383550684055 | 0.0013104379221241737 | 10 |
| 14 | {'clf__C': 100, 'clf__loss': 'squared_hinge', 'vect__ngram_range': (1, 1), 'vect__use_idf': False} | 0.9999799237100984 | 4.015257980323206e-05 | 0.9724777982238579 | 0.000490052042907041 | 19 |
| 15 | {'clf__C': 100, 'clf__loss': 'squared_hinge', 'vect__ngram_range': (1, 2), 'vect__use_idf': True} | 0.9999799237100984 | 4.015257980323206e-05 | 0.982238579086327 | 0.0015522557964587798 | 3 |
| 16 | {'clf__C': 100, 'clf__loss': 'squared_hinge', 'vect__ngram_range': (1, 2), 'vect__use_idf': False} | 0.9999799237100984 | 4.015257980323206e-05 | 0.9769581566525322 | 0.001880732826022944 | 16 |
| 17 | {'clf__C': 1000, 'clf__loss': 'hinge', 'vect__ngram_range': (1, 1), 'vect__use_idf': True} | 0.9999799237100984 | 4.015257980323206e-05 | 0.9791183294663574 | 0.0014083901129112494 | 11 |
| 18 | {'clf__C': 1000, 'clf__loss': 'hinge', 'vect__ngram_range': (1, 1), 'vect__use_idf': False} | 0.9999799237100984 | 4.015257980323206e-05 | 0.9718377470197616 | 0.0010911334240913265 | 24 |
| 19 | {'clf__C': 1000, 'clf__loss': 'hinge', 'vect__ngram_range': (1, 2), 'vect__use_idf': True} | 0.9999799237100984 | 4.015257980323206e-05 | 0.9817585406832546 | 0.0023122309922603943 | 6 |
| 20 | {'clf__C': 1000, 'clf__loss': 'hinge', 'vect__ngram_range': (1, 2), 'vect__use_idf': False} | 0.9999799237100984 | 4.015257980323206e-05 | 0.976558124649972 | 0.0022704550312480894 | 17 |
| 21 | {'clf__C': 1000, 'clf__loss': 'squared_hinge', 'vect__ngram_range': (1, 1), 'vect__use_idf': True} | 0.9999799237100984 | 4.015257980323206e-05 | 0.9791183294663574 | 0.0014083901129112494 | 11 |
| 22 | {'clf__C': 1000, 'clf__loss': 'squared_hinge', 'vect__ngram_range': (1, 1), 'vect__use_idf': False} | 0.9999799237100984 | 4.015257980323206e-05 | 0.9719177534202736 | 0.0011153206214202123 | 23 |
| 23 | {'clf__C': 1000, 'clf__loss': 'squared_hinge', 'vect__ngram_range': (1, 2), 'vect__use_idf': True} | 0.9999799237100984 | 4.015257980323206e-05 | 0.9818385470837667 | 0.0021539947740467995 | 5 |
| 24 | {'clf__C': 1000, 'clf__loss': 'squared_hinge', 'vect__ngram_range': (1, 2), 'vect__use_idf': False} | 0.9999799237100984 | 4.015257980323206e-05 | 0.97647811824946 | 0.0022131520530953913 | 18 |



# Test check

| name | score |
| --- | --- |
| No overlap SVC | 97.38 |
| No overlap LinearSVC | 98.05 |
| With overlap SVC | 99.29 |
| With overlap LinearSVC | 99.73 |
