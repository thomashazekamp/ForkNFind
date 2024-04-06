import React from 'react';
import { render, waitFor } from '@testing-library/react-native';
import EditReviewScreen from '../EditReviewScreen';
import { create } from 'react-test-renderer';

describe('EditReviewScreen', () => {
    // mock the review data, needed for the screen
    const mockReviewData = {
        name: 'Test Name',
        description: 'Nice',
        rating: 4,
        restaurant: {
            name: 'Test Restaurant'
        },
    };

    it('Should have 3 children', () => {
        // check that the screen has 3 children
        const tree = create(<EditReviewScreen reviewData={mockReviewData} />).toJSON();
        expect(tree.children.length).toBe(3);
    });

    it('Should have a snapshot', () => {
        // check that the screen matches the snapshot
        const tree = create(<EditReviewScreen reviewData={mockReviewData} />).toJSON();
        expect(tree).toMatchSnapshot();
    });
    
    it('Should have Your Rating', async () => {
        // render the review screen with a given data
        const { getByText } = render(<EditReviewScreen reviewData={mockReviewData} />);
        // wait for the network request to complete
        await waitFor(() => getByText('Your Rating'), {timeout: 10000});
        // check that the screen has rendered
        expect(getByText('Your Rating')).toBeTruthy();
    });
    it('Should have adding review', async () => {
        // render the review screen with a given data
        const { getByText } = render(<EditReviewScreen reviewData={mockReviewData} />);
        // wait for the network request to complete
        await waitFor(() => getByText('Add detailed Review'), {timeout: 10000});
        // check that the screen has rendered
        expect(getByText('Add detailed Review')).toBeTruthy();
    });
    it('Should have Update', async () => {
        // render the review screen with a given data
        const { getByText } = render(<EditReviewScreen reviewData={mockReviewData} />);
        // wait for the network request to complete
        await waitFor(() => getByText('Update'), {timeout: 10000});
        // check that the screen has rendered
        expect(getByText('Update')).toBeTruthy();
    });
});