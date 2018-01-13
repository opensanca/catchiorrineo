import accountReducer from './account';
import adoptionReducer from './adoption';
import animalReducer from './animal';

import { createStore, combineReducers } from 'redux'

const reducers = combineReducers({
    account: accountReducer,
    adoption: adoptionReducer,
    animal: animalReducer,
})

export default createStore(reducers);