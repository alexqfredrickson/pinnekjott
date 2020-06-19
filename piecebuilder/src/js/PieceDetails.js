import React from 'react';
import '../css/PieceDetails.css';

class PieceDetails extends React.Component {
  constructor(props) {
    super(props);
    
    this.state = {
      buttonCount: null,
      turnCount: null,
      cost: null,
    };
    
    this.handleButtonCountChange = this.handleButtonCountChange.bind(this);
    this.handleTurnCountChange = this.handleTurnCountChange.bind(this);
    this.handleCostChange = this.handleCostChange.bind(this);

    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleButtonCountChange(event) {
    this.setState({value: event.target.value});
  }

  handleTurnCountChange(event) {
    this.setState({value: event.target.value});
  }

  handleCostChange(event) {
    this.setState({value: event.target.value});
  }

  handleSubmit(event) {
    alert('A name was submitted: ' + this.state.value);
    event.preventDefault();
  }

  render() {
    return (
      <form className="piece-details" onSubmit={this.handleSumbit}>
        
        <label>Button Count</label>
        <br/>

        <input type="text" value={this.state.buttonCount} onChange={this.handleButtonCountChange} />
        <br/>
                
        <label>Turn Count</label>
        <br/>
        
        <input type="text" value={this.state.turnCount} onChange={this.handleTurnCountChange} />
        <br/>
        
        <label>Cost</label>
        <br/>
        
        <input type="text" value={this.state.cost} onChange={this.handleCostChange} />
        <br/>
        
        <input type="submit" value="Register Piece" />
      </form>
    );
  };
}
  
export default PieceDetails;
  