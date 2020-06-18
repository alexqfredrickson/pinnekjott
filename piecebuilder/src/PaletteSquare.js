import React from 'react';
import './PaletteSquare.css';

class PaletteSquare extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      isSelected: false
    };

    this.handleClick = this.handleClick.bind(this);
  }

  handleClick() {    
    this.setState(state => ({      
      isSelected: !state.isSelected    
    }));
  }

  render() {
    return (
      <div 
        className={"PaletteSquare " + (this.state.isSelected ? 'bg-green' : 'bg-white')}
        onClick={this.handleClick}
      >
      </div>
    );
  };
}
  
export default PaletteSquare;
  