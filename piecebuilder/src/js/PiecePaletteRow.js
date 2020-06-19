import React from 'react';
import '../css/PiecePaletteRow.css';
import PiecePaletteSquare from './PiecePaletteSquare.js';

class PiecePaletteRow extends React.Component {

  render() {

    const squares = Array.from(this.props.row).map((item, i) => 

      <PiecePaletteSquare 
        key={i} 
        rowNumber={this.props.row[i][0]} 
        columnNumber={this.props.row[i][1]}
        isSelected={this.props.row[i][2]}
        squareClicker={this.props.squareClicker}
      />

    );

    return (
      <div className="piece-palette-row">{squares}</div>
    );
  };
}
  
export default PiecePaletteRow;
  