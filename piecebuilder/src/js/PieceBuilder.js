import React from 'react';
import '../css/PieceBuilder.css';
import PiecePalette from './PiecePalette.js';
import PiecePreview from './PiecePreview.js';
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
      <div className="container-fluid piece-builder">
        <div className="row">
          <div className="col-6">
            <PiecePalette grid={this.state.grid} squareClicker={this.handleClick} />
          </div>
          <div className="col-6">
            <PiecePreview />
          </div>
        </div>
        
        <div className="row">
          <PieceDetails />
        </div>    
      </div>
      );
  };
}

export default PieceBuilder;
