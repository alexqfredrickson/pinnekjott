import React from 'react';
import './PaletteRow.css';
import PaletteSquare from './PaletteSquare.js';

class PaletteRow extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    const paletteSquares = Array.from(Array(5).keys()).map(
      function(item, i) {
        return <PaletteSquare key={i} /> 
      }
    );

    return (
      <div className="PaletteRow">{paletteSquares}</div>
    );
  };
}
  
export default PaletteRow;
  