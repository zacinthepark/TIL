### Random Search, Grid Search

- Grid Search 범위를 적게 하여 찾은 값을 기준으로 파라미터 범위를 조정하여 Grid Search를 다시 해보는 것 고려
- Random Search를 통해 찾은 값을 기준으로 파라미터 범위를 조정하여 Grid Search를 해보는 것도 고려

### Hyperparameter 튜닝

> 1. 기본 모델 설정 (model_default)
> 2. 성능을 검증하고자 할 Hyperparameter 값 범위 설정
> 3. 기본 모델을 바탕으로 RandomizedSearchCV, GridSearchCV를 활용하여 다양한 모델 검증
> 3-1. CV가 들어간다는 것은 검증 방식에 k 분할 교차 검증 방식이 사용된다는 것
> 4. model.best_estimator_를 통해 최적 파라미터를 적용한 모델에 접근

- GridSearch는 모든 파라미터 조합에 대한 성능을 확인하여 베스트 파라미터를 찾는 것
- RandomSearch는 n_iter 지정
- 학습 데이터에 대한 성능에서는 GridSearch보다 RandomSearch가 더 좋은 성능을 파라미터를 찾는 경우는 없을 것
- 하지만 해당 파라미터(max_depth, n_neighbors)가 학습 데이터에 대한 성능은 좋을지 몰라도 이것이 곧 평가 데이터에서 성능이 좋을 것이라는 것을 보장하지는 않는다
- 고로 RandomSearch를 통해 얻은 최적의 파라미터가 GridSearch를 통해 얻은 최적의 파라미터보다 평가 데이터에 대해서는 성능이 좋을 수 있다
