import React from 'react';
import './PiecePalette.css';
import PiecePaletteRow from './PiecePaletteRow.js';

class PiecePalette extends React.Component {
  
  render() {
    const rows = Array.from(this.props.grid).map(
      (item, i) => <PiecePaletteRow key={i} row={this.props.grid[i]} squareClicker={this.props.squareClicker} />
    );

    return (<div className="piece-palette">{rows}</div>);
  };
}
  
export default PiecePalette;
  