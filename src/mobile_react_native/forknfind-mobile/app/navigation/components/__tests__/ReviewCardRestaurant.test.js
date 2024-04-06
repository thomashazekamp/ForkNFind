import React from 'react';
import { render, waitFor } from '@testing-library/react-native';
import ReviewCardRestaurant from '../ReviewCardRestaurant';
import { create } from 'react-test-renderer';

describe('ReviewCardRestaurant', () => {
    // mock the review data, needed for the screen
    const mockData = {
        restaurant: {
            name: 'Test Restaurant',
        },
        rating: 4,
        description: 'Nice place',
        sentiment: '1',
        date: '01/01/2024',
    };

    it('Should have 3 children', () => {
        // check that the screen has 3 children
        const tree = create(<ReviewCardRestaurant data={mockData} />).toJSON();
        expect(tree.children.length).toBe(3);
    });

    it('Should have a snapshot', () => {
        // check that the screen matches the snapshot
        const tree = create(<ReviewCardRestaurant data={mockData} />).toJSON();
        expect(tree).toMatchSnapshot();
    });
    
    it('Should have name', () => {
        // render the review screen with a given data
        const { getByText } = render(<ReviewCardRestaurant data={mockData} />);
        // check that the screen has rendered
        expect(getByText(mockData.restaurant.name)).toBeTruthy();
    });

    it('Should have desc', () => {
        // render the review screen with a given data
        const { getByText } = render(<ReviewCardRestaurant data={mockData} />);
        // check that the screen has rendered
        expect(getByText(mockData.description)).toBeTruthy();
    });

    it('Should have date', () => {
        // render the review screen with a given data
        const { getByText } = render(<ReviewCardRestaurant data={mockData} />);
        // check that the screen has rendered
        expect(getByText(mockData.date)).toBeTruthy();
    });
});