import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import PieceBuilder from './js/PieceBuilder';
import * as serviceWorker from './serviceWorker';

ReactDOM.render(
  <React.StrictMode>
    <PieceBuilder />
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
