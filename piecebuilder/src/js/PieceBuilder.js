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
      ),
      numpyStrings: []
    }

    this.handleClick = this.handleClick.bind(this);
  }

  getGridAsNumpyString() {

    let grid = Array.from(this.state.grid);

    const rowIsEmpty = (sq) => sq[2] == false;  // sq[2] == false means the square is not selected 
    
    // remove empty rows
    grid = grid.filter(r => !r.every(rowIsEmpty));

    // if everything is empty, return null
    if (grid[0] === undefined) {
      return "";
    }

    // remove empty columns; hack: transpose matrix, remove empty rows, untranspose matrix 
    grid = grid[0].map((_, colIndex) => grid.map(row => row[colIndex]));
    grid = grid.filter(r => !r.every(rowIsEmpty));
    grid = grid[0].map((_, colIndex) => grid.map(row => row[colIndex]));

    let numpyString = "np.array([";

    for (let i = 0; i < grid.length; i++) {
      numpyString = numpyString + "[";

      for (let j = 0; j < grid[i].length; j++) {
        if (grid[i][j][2] == true) {
          numpyString = numpyString + "True, " 
        } else {
          numpyString = numpyString + "False, "
        }
      }  
      numpyString = numpyString.slice(0, -2) + "],"
    }

    numpyString = numpyString.slice(0, -1) + "]),\n";

    return numpyString;
  }

  

  handleClick(e, rowNumber, columnNumer, isSelected) {
    
    let newGrid = Array.from(this.state.grid);
    newGrid[rowNumber][columnNumer] = [rowNumber, columnNumer, isSelected]

    let newNumpyStrings = Array.from(this.state.numpyStrings);
    let currentNumpyString = this.getGridAsNumpyString();
    newNumpyStrings.push(currentNumpyString);

    this.setState({
      grid: newGrid,
      numpyStrings: [currentNumpyString]
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
            <PiecePreview preview={this.state.numpyStrings}/>
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
