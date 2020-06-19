import React from 'react';
import '../css/PiecePaletteSquare.css';

class PiecePaletteSquare extends React.Component {

  render() {
    return (
      <div 
        className={"palette-square " + (this.props.isSelected ? 'bg-green' : 'bg-white')}
        onClick={(e, rowNumber, columnNumber, isSelected) => 
          this.props.squareClicker(e, this.props.rowNumber, this.props.columnNumber, !this.props.isSelected)}
      />
    );
  };
}
  
export default PiecePaletteSquare;
  