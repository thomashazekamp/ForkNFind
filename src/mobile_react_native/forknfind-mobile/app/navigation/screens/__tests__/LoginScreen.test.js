/* 
Reference: https://www.youtube.com/watch?v=PlppJvJ67GA&ab_channel=MissCoding
*/
import React from 'react';
import { render, waitFor } from '@testing-library/react-native';
import { create } from 'react-test-renderer';
import LoginScreen from '../LoginScreen';

describe('LoginScreen', () => {

    it('Should have 1 children', () => {
        // check that the screen has 3 children
        const tree = create(<LoginScreen />).toJSON();
        expect(tree.children.length).toBe(1);
    });

    it('Should have a snapshot', () => {
        // check that the screen matches the snapshot
        const tree = create(<LoginScreen />).toJSON();
        expect(tree).toMatchSnapshot();
    });
    
    it('Should have Sign In', () => {
        // render the review screen with a given data
        const { getAllByText } = render(<LoginScreen />);
        // check that the screen has rendered
        expect(getAllByText('Sign In').length).toBeGreaterThan(0);
    });
});