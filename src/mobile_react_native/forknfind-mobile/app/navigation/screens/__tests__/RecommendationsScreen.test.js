/* 
Reference: https://www.youtube.com/watch?v=PlppJvJ67GA&ab_channel=MissCoding
*/
import React from 'react';
import { render, waitFor } from '@testing-library/react-native';
import { create } from 'react-test-renderer';
import RecommendationsScreen from '../RecommendationsScreen';

describe('RecommendationsScreen', () => {

    global.access_global = 'token_test' // used to mock the access token

    it('Should have 2 children', () => {
        // check that the screen has 3 children
        const tree = create(<RecommendationsScreen />).toJSON();
        expect(tree.children.length).toBe(2);
    });

    it('Should have a snapshot', () => {
        // check that the screen matches the snapshot
        const tree = create(<RecommendationsScreen />).toJSON();
        expect(tree).toMatchSnapshot();
    });
});