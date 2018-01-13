import { Provider } from 'react-redux'
import { Router, Route, browserHistory } from 'react-router'
import { syncHistoryWithStore, routerReducer } from 'react-router-redux'

import store from './data-flow/store';

const history = syncHistoryWithStore(browserHistory, store)

export const App = () => (
    <Provider store={store}>
        <Router history={history}>
            <Route path="/" component={Test} />
        </Router>
    </Provider>
);

export default App;