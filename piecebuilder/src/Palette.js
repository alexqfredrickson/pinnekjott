import React from 'react';
import './Palette.css';
import PaletteRow from './PaletteRow.js';

class Palette extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    const paletteRows = Array.from(Array(5).keys()).map(
      function(item, i) {
        return <PaletteRow key={i} /> 
      }
    );

    return (
      <div className="Palette">{paletteRows}</div>
    );
  };
}

export default Palette;
