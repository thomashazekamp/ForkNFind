import React from 'react';
import { render, waitFor } from '@testing-library/react-native';
import ReviewCard from '../ReviewCard';
import { create } from 'react-test-renderer';

describe('ReviewCard', () => {
    // mock the review data, needed for the screen
    const mockData = {
        restaurant: {
            name: 'Test Restaurant',
        },
        rating: 4,
        description: 'Nice place',
        sentiment: '1',
    };

    global.Platform = 'ios' // used to mock the platform
    global.access_global = 'token_test' // used to mock the access token

    it('Should have 3 children', () => {
        // check that the screen has 3 children
        const tree = create(<ReviewCard data={mockData} />).toJSON();
        expect(tree.children.length).toBe(3);
    });

    it('Should have a snapshot', () => {
        // check that the screen matches the snapshot
        const tree = create(<ReviewCard data={mockData} />).toJSON();
        expect(tree).toMatchSnapshot();
    });
    
    it('Should have name', () => {
        // render the review screen with a given data
        const { getByText } = render(<ReviewCard data={mockData} />);
        // check that the screen has rendered
        expect(getByText(mockData.restaurant.name)).toBeTruthy();
    });

    it('Should have name', () => {
        // render the review screen with a given data
        const { getByText } = render(<ReviewCard data={mockData} />);
        // check that the screen has rendered
        expect(getByText(mockData.description)).toBeTruthy();
    });
});