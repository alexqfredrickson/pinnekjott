import React from 'react';
import './PiecePreview.css';

class PiecePreview extends React.Component {

  // https://stackoverflow.com/questions/41233458/react-child-component-not-updating-after-parent-state-change
  componentWillReceiveProps(nextProps) {
    this.setState({ numpyData: nextProps.preview });  
  }

  render() {
    return (
      <div className="piece-preview">
        <textarea className="form-control" value={this.props.preview}></textarea>
      </div>
      );
  };
}

export default PiecePreview;
