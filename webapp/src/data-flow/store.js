import accountReducer from './account/reducer';
import adoptionReducer from './adoption/reducer';
import animalReducer from './animal/reducer';

import { createStore, combineReducers } from 'redux'

const reducers = combineReducers({
    account: accountReducer,
    adoption: adoptionReducer,
    animal: animalReducer,
})

export default createStore(reducers);