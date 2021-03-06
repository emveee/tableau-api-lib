from tableau_api_lib.api_requests import BaseRequest


class AddViewToFavoritesRequest(BaseRequest):
    """
    Builds the request body for Tableau Server REST API requests adding views to favorites.
    :param class ts_connection: the Tableau Server connection object
    :param str favorite_label: the text label to assign to the favorite item
    :param str view_id: the view ID
    """
    def __init__(self,
                 ts_connection,
                 favorite_label,
                 view_id):

        super().__init__(ts_connection)
        self._favorite_label = favorite_label
        self._view_id = view_id

    def base_add_favorites_request(self):
        self._request_body.update({
            'favorite': {
                'label': self._favorite_label,
                'view': {'id': self._view_id}
            }
        })
        return self._request_body

    def get_request(self):
        return self.base_add_favorites_request()
