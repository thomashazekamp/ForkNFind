import React from 'react';
import { render, waitFor } from '@testing-library/react-native';
import RestaurantSortBy from '../RestaurantSortBy';
import { create } from 'react-test-renderer';

describe('RestaurantSortBy', () => {
    // mock the review data, needed for the screen
    const mockData = {
        id: '1',
        name: 'Test Restaurant',
        type: 'Italian',
        price_level: '3',
        average_rating: 4.3,
        distance_from_user: 2,
        open_or_close: 'Open',
        review_number: 1,
      };

    it('Should have 3 children', () => {
        // check that the screen has 3 children
        const tree = create(<RestaurantSortBy restaurantData={mockData} />).toJSON();
        expect(tree.children.length).toBe(3);
    });

    it('Should have a snapshot', () => {
        // check that the screen matches the snapshot
        const tree = create(<RestaurantSortBy restaurantData={mockData} />).toJSON();
        expect(tree).toMatchSnapshot();
    });
    
    it('Should have relevance', () => {
        // render the review screen with a given data
        const { getByText } = render(<RestaurantSortBy restaurantData={mockData} />);
        // check that the screen has rendered
        expect(getByText('Relevance')).toBeTruthy();
    });

    it('Should have Ratings (Ascending)', () => {
        // render the review screen with a given data
        const { getByText } = render(<RestaurantSortBy restaurantData={mockData} />);
        // check that the screen has rendered
        expect(getByText('Ratings (Ascending)')).toBeTruthy();
    });

    it('Should have Ratings (Descending)', () => {
        // render the review screen with a given data
        const { getByText } = render(<RestaurantSortBy restaurantData={mockData} />);
        // check that the screen has rendered
        expect(getByText('Ratings (Descending)')).toBeTruthy();
    });

    it('Should have Alphabetical', () => {
        // render the review screen with a given data
        const { getByText } = render(<RestaurantSortBy restaurantData={mockData} />);
        // check that the screen has rendered
        expect(getByText('Alphabetical (A - Z)')).toBeTruthy();
    });

    it('Should have back', () => {
        // render the review screen with a given data
        const { getByText } = render(<RestaurantSortBy restaurantData={mockData} />);
        // check that the screen has rendered
        expect(getByText('Back')).toBeTruthy();
    });

    it('Should have apply', () => {
        // render the review screen with a given data
        const { getByText } = render(<RestaurantSortBy restaurantData={mockData} />);
        // check that the screen has rendered
        expect(getByText('Apply')).toBeTruthy();
    });
});