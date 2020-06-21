import React from 'react';
import '../css/PiecePreview.css';

class PiecePreview extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      numpyData: this.props.preview
    }
  }

  // https://stackoverflow.com/questions/41233458/react-child-component-not-updating-after-parent-state-change
  componentWillReceiveProps(nextProps) {
    this.setState({ numpyData: nextProps.preview });  
  }

  render() {
    return (
      <div className="piece-preview">{this.state.numpyData}</div>
      );
  };
}

export default PiecePreview;
