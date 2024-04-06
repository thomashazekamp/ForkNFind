import React from 'react';
import { render, waitFor } from '@testing-library/react-native';
import MapFilter from '../MapFilter';
import { create } from 'react-test-renderer';

describe('MapFilter', () => {
    // mock the review data, needed for the screen
    const mockReviewData = {
        name: 'Test Name',
        description: 'Nice',
        rating: 4,
        restaurant: {
            name: 'Test Restaurant'
        },
    };

    it('Should have 2 children', () => {
        // check that the screen has 3 children
        const tree = create(<MapFilter />).toJSON();
        expect(tree.children.length).toBe(2);
    });

    it('Should have a snapshot', () => {
        // check that the screen matches the snapshot
        const tree = create(<MapFilter />).toJSON();
        expect(tree).toMatchSnapshot();
    });
    
    it('Should have Open', async () => {
        // render the review screen with a given data
        const { getByText } = render(<MapFilter />);
        // wait for the network request to complete
        await waitFor(() => getByText('Open'), {timeout: 10000});
        // check that the screen has rendered
        expect(getByText('Open')).toBeTruthy();
    });
    it('Should have Closed', async () => {
        // render the review screen with a given data
        const { getByText } = render(<MapFilter />);
        // wait for the network request to complete
        await waitFor(() => getByText('Closed'), {timeout: 10000});
        // check that the screen has rendered
        expect(getByText('Closed')).toBeTruthy();
    });
    it('Should have Recommended', async () => {
        // render the review screen with a given data
        const { getByText } = render(<MapFilter />);
        // wait for the network request to complete
        await waitFor(() => getByText('Recommended'), {timeout: 10000});
        // check that the screen has rendered
        expect(getByText('Recommended')).toBeTruthy();
    });
    it('Should have All', async () => {
        // render the review screen with a given data
        const { getByText } = render(<MapFilter />);
        // wait for the network request to complete
        await waitFor(() => getByText('All'), {timeout: 10000});
        // check that the screen has rendered
        expect(getByText('All')).toBeTruthy();
    });
    it('Should have Apply', async () => {
        // render the review screen with a given data
        const { getByText } = render(<MapFilter />);
        // wait for the network request to complete
        await waitFor(() => getByText('Apply'), {timeout: 10000});
        // check that the screen has rendered
        expect(getByText('Apply')).toBeTruthy();
    });
});