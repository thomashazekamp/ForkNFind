import React from 'react';
import renderer from 'react-test-renderer';

import MainContainer from '../MainContainer';

describe('<MainContainer />', () => {
//   it('has 1 child', () => {
//     const tree = renderer.create(<App />).toJSON();
//     expect(tree.children.length).toBe(1);
//   });

  it('renders correctly', () => {
    const tree = renderer.create(<MainContainer />).toJSON();
    expect(tree).toMatchSnapshot();
  });
});