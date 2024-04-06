import React from 'react';
import { render, waitFor } from '@testing-library/react-native';
import ReviewSortBy from '../ReviewSortBy';
import { create } from 'react-test-renderer';

describe('ReviewSortBy', () => {
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
        const tree = create(<ReviewSortBy data={mockData} />).toJSON();
        expect(tree.children.length).toBe(3);
    });

    it('Should have a snapshot', () => {
        // check that the screen matches the snapshot
        const tree = create(<ReviewSortBy data={mockData} />).toJSON();
        expect(tree).toMatchSnapshot();
    });
    
    it('Should have relevance', () => {
        // render the review screen with a given data
        const { getByText } = render(<ReviewSortBy data={mockData} />);
        // check that the screen has rendered
        expect(getByText('Relevance')).toBeTruthy();
    });

    it('Should have Back', () => {
        // render the review screen with a given data
        const { getByText } = render(<ReviewSortBy data={mockData} />);
        // check that the screen has rendered
        expect(getByText('Back')).toBeTruthy();
    });

    it('Should have Apply', () => {
        // render the review screen with a given data
        const { getByText } = render(<ReviewSortBy data={mockData} />);
        // check that the screen has rendered
        expect(getByText('Apply')).toBeTruthy();
    });
});