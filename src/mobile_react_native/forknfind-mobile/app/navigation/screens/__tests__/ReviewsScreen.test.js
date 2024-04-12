/* 
Reference: https://www.youtube.com/watch?v=PlppJvJ67GA&ab_channel=MissCoding
*/
import React from 'react';
import { render, waitFor } from '@testing-library/react-native';
import { create } from 'react-test-renderer';
import ReviewsScreen from '../ReviewsScreen';

jest.mock('@react-navigation/native', () => ({
    ...jest.requireActual('@react-navigation/native'),
    useFocusEffect: jest.fn(),
}));

describe('ReviewsScreen', () => {

    global.access_global = 'token_test' // used to mock the access token

    it('Should have 2 children', () => {
        // check that the screen has 3 children
        const tree = create(<ReviewsScreen />).toJSON();
        expect(tree.children.length).toBe(2);
    });

    /* it('Should have a snapshot', () => {
        // check that the screen matches the snapshot
        const tree = create(<ReviewsScreen />).toJSON();
        expect(tree).toMatchSnapshot();
    }); */
    
    it('Should have Positive', () => {
        // render the review screen with a given data
        const { getByText } = render(<ReviewsScreen />);
        // check that the screen has rendered
        expect(getByText('Positive')).toBeTruthy();
    });

    it('Should have Negative', () => {
        // render the review screen with a given data
        const { getByText } = render(<ReviewsScreen />);
        // check that the screen has rendered
        expect(getByText('Negative')).toBeTruthy();
    });

    it('Should have All', () => {
        // render the review screen with a given data
        const { getByText } = render(<ReviewsScreen />);
        // check that the screen has rendered
        expect(getByText('All')).toBeTruthy();
    });
});