import React from 'react';
import '../css/PieceBuilder.css';
import PiecePalette from './PiecePalette.js';
import PieceDetails from './PieceDetails.js';

class PieceBuilder extends React.Component {

  constructor(props) {
    super(props);

    this.state = {
      grid: Array.from(Array(5).keys()).map(
        i => Array.from(Array(5).keys()).map(
          j => [i, j, false]
        )
      )  
    }

    // console.log(this.state.grid);

    this.handleClick = this.handleClick.bind(this);
  }

  handleClick(e, rowNumber, columnNumer, isSelected) {
    
    let newGrid = Array.from(this.state.grid);
    newGrid[rowNumber][columnNumer] = [rowNumber, columnNumer, isSelected]

    this.setState({
      grid: newGrid
    });
  }

  render() {
    return (
      <div className="piece-builder">
        <PiecePalette grid={this.state.grid} squareClicker={this.handleClick} />
        <PieceDetails />    
      </div>
      );
  };
}

export default PieceBuilder;
