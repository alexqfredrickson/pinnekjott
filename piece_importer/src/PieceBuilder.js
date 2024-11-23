import React from 'react';
import './PieceBuilder.css';
import PiecePalette from './PiecePalette.js';
import PiecePreview from './PiecePreview.js';
import PieceDetails from './PieceDetails.js';
import PieceBuilderInfo from './PieceBuilderInfo.js';

class PieceBuilder extends React.Component {

  constructor(props) {
    super(props);

    this.state = {
      grid: Array.from(Array(5).keys()).map(
        i => Array.from(Array(5).keys()).map(
          j => [i, j, false]
        )
      ),
      buttonCount: "",
      turnCount: "",
      cost: "",
      name: "",
      currentNumpyStringFromGrid: "",
      pinnekjottString: ""
    }

    this.handleGridClick = this.handleGridClick.bind(this);
    this.handleSavePiece = this.handleSavePiece.bind(this);
    this.handleChangeButtonCount = this.handleChangeButtonCount.bind(this);
    this.handleChangeTurnCount = this.handleChangeTurnCount.bind(this);
    this.handleChangeCost = this.handleChangeCost.bind(this);
    this.handleChangeName = this.handleChangeName.bind(this);
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
          numpyString = numpyString + "1, "
        } else {
          numpyString = numpyString + "0, "
        }
      }  
      numpyString = numpyString.slice(0, -2) + "],"
    }

    numpyString = numpyString.slice(0, -1) + "])";

    return numpyString;
  }

  handleGridClick(e, rowNumber, columnNumer, isSelected) {
    let newGrid = Array.from(this.state.grid);
    newGrid[rowNumber][columnNumer] = [rowNumber, columnNumer, isSelected]

    let currentNumpyStringFromGrid = this.getGridAsNumpyString();

    this.setState({
      grid: newGrid,
      currentNumpyStringFromGrid: currentNumpyStringFromGrid,
    });

    document.getElementById("buttonCountInput").focus();
  }

  handleSavePiece(event) {
    event.preventDefault();

    // get new pinnekjott string, like this:
    // 
    //    Piece(
    //       squares=np.array([True, False]),
    //       buttons=0,
    //       turns=1,
    //       cost=2
    //    ),
    //

    let pinnekjottString = "\nPiece(";
    pinnekjottString = pinnekjottString + "\n    " + "base_orientation=" + this.state.currentNumpyStringFromGrid + ",";
    pinnekjottString = pinnekjottString + "\n    " + "buttons=" + this.state.buttonCount + ",";
    pinnekjottString = pinnekjottString + "\n    " + "time_cost=" + this.state.turnCount + ",";
    pinnekjottString = pinnekjottString + "\n    " + "button_cost=" + this.state.cost + "";
    pinnekjottString = pinnekjottString + "\n    " + "name=" + this.state.cost + "";
    pinnekjottString = pinnekjottString + "\n),";

    this.setState({
      grid: Array.from(Array(5).keys()).map(
        i => Array.from(Array(5).keys()).map(
          j => [i, j, false]
        )
      ),
      buttonCount: "",
      turnCount: "",
      cost: "",
      name: "",
      currentNumpyStringFromGrid: "",
      pinnekjottString: this.state.pinnekjottString + pinnekjottString
    });

    console.log("A new Pinnekjott string has been generated:");
    console.log(this.state.pinnekjottString);
  }

  handleChangeButtonCount(event) {
    this.setState({buttonCount: event.target.value});
    console.log("Changed button count.");
    console.log(event.target.value);
  }

  handleChangeTurnCount(event) {
    this.setState({turnCount: event.target.value});
    console.log("Changed turn count.");
  }

  handleChangeCost(event) {
    this.setState({cost: event.target.value});
    console.log("Changed button cost.");
  }

  handleChangeName(event) {
    this.setState({name: event.target.value});
    console.log("Changed name.");
  }

  render() {
    return (
      <div className="container-fluid piece-builder">
        
        <div className="row">
          <div className="col-8">
            <PieceBuilderInfo />
          </div>

          <div className="col-4">
            <PiecePalette grid={this.state.grid} squareClicker={this.handleGridClick} />
          </div>  
        </div>
        
        <div className="row">
          <div className="col-4">
            <PieceDetails 
              buttonCount={this.state.buttonCount} 
              buttonCountChanger={this.handleChangeButtonCount} 
              turnCount={this.state.turnCount} 
              turnCountChanger={this.handleChangeTurnCount}
              cost={this.state.cost} 
              costChanger={this.handleChangeCost}
              name={this.state.name}
              nameChanger={this.handleChangeName}
              pieceSaver={this.handleSavePiece} 
            />
          </div>

          <div className="col-8">
            <PiecePreview preview={this.state.pinnekjottString}/>
          </div>
        </div>    

      </div>
      );
  };
}

export default PieceBuilder;
