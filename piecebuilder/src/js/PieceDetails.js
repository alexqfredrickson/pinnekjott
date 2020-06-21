import React from 'react';
import '../css/PieceDetails.css';

class PieceDetails extends React.Component {
  render() {
    return (
      <form className="piece-details" onSubmit={this.props.pieceSaver}>
        <label>Button Count</label>
        <br/>

        <input type="text" value={this.props.buttonCount} onChange={this.handleButtonCountChange} />
        <br/>
                
        <label>Turn Count</label>
        <br/>
        
        <input type="text" value={this.props.turnCount} onChange={this.handleTurnCountChange} />
        <br/>
        
        <label>Cost</label>
        <br/>
        
        <input type="text" value={this.props.cost} onChange={this.handleCostChange} />
        <br/><br/>
        
        <input type="submit" value="Save Piece" />
      </form>
    );
  };
}
  
export default PieceDetails;
  