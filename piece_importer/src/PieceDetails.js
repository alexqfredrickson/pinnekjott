import React from 'react';
import './PieceDetails.css';

class PieceDetails extends React.Component {
  render() {
    return (
      <form className="piece-details form-group" onSubmit={this.props.pieceSaver}>
        <label>Button Count</label>
        <br/>

        <input 
          id="buttonCountInput"
          className="form-control" 
          type="text" 
          value={this.props.buttonCount} 
          onChange={this.props.buttonCountChanger}
        />
        
        <br/>
                
        <label>Cost</label>
        <br/>
        
        <input className="form-control" type="text" value={this.props.cost} onChange={this.props.costChanger} />
        <br/>
        
        <label>Turn Count</label>
        <br/>
        
        <input className="form-control" type="text" value={this.props.turnCount} onChange={this.props.turnCountChanger} />
        <br/>

        <label>Piece Name</label>
        <br/>

        <input className="form-control" type="text" value={this.props.name} onChange={this.props.nameChanger} />
        <br/>
                
        <input className="btn" type="submit" value="Save Piece" />
      </form>
    );
  };
}
  
export default PieceDetails;
  