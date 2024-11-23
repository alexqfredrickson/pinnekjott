import React from 'react';
import './PieceBuilderInfo.css';

class PieceBuilderInfo extends React.Component {

  render() {
    return (
      <form className="piece-builder-info">
        <h1>Pinnekjott Piece Builder</h1>
        <br/>
        <ul>
          <li>Click squares in the grid - make sure the selected area is contiguous.</li>
          <li>Add metadata.</li>
          <li>Click 'Save Piece' - this generates a Pinnekjott-friendly string representing a piece.</li>
        </ul>
      </form>
    );
  };
}
  
export default PieceBuilderInfo;
  