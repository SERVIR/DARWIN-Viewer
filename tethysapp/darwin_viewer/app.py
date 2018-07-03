from tethys_sdk.base import TethysAppBase, url_map_maker

class DarwinViewer(TethysAppBase):
    """
    Tethys app class for RHEAS Viewer.
    """

    name = 'DARWIN Viewer'
    index = 'darwin_viewer:home'
    icon = 'darwin_viewer/images/logo.png'
    package = 'darwin_viewer'
    root_url = 'darwin-viewer'
    color = '#27ae60'
    description = 'View RHEAS data from darwin'
    tags = 'Hydrology'
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='darwin-viewer',
                controller='darwin_viewer.controllers.home'
            ),
            UrlMap(
                name='vic',
                url='darwin-viewer/vic',
                controller='darwin_viewer.controllers.vic'
            ),
            UrlMap(
                name='schemas',
                url='darwin-viewer/vic/schemas',
                controller='darwin_viewer.ajax_controllers.get_db_schemas'
            ),
            UrlMap(
                name='variables',
                url='darwin-viewer/vic/variables',
                controller='darwin_viewer.ajax_controllers.get_vars'
            ),
            UrlMap(
                name='dates',
                url='darwin-viewer/vic/dates',
                controller='darwin_viewer.ajax_controllers.get_dates'
            ),
            UrlMap(
                name='raster',
                url='darwin-viewer/vic/raster',
                controller='darwin_viewer.ajax_controllers.get_raster'
            ),
            UrlMap(
                name='bounds',
                url='darwin-viewer/vic/bounds',
                controller='darwin_viewer.ajax_controllers.get_bounds'
            ),
            UrlMap(
                name='bounds',
                url='darwin-viewer/dssat/bounds',
                controller='darwin_viewer.ajax_controllers.get_bounds'
            ),
            UrlMap(
                name='get-vic-plot',
                url='darwin-viewer/vic/get-vic-plot',
                controller='darwin_viewer.ajax_controllers.get_vic_plot'
            ),
            UrlMap(
                name='dssat',
                url='darwin-viewer/dssat',
                controller='darwin_viewer.controllers.dssat'
            ),
            UrlMap(
                name='dssat-schema',
                url='darwin-viewer/dssat/schemas',
                controller='darwin_viewer.ajax_controllers.get_dssat_schemas'
            ),
            UrlMap(
                name='dsensemble',
                url='darwin-viewer/dssat/get-ensemble',
                controller='darwin_viewer.ajax_controllers.get_ensemble'
            ),
            UrlMap(
                name='dsensval',
                url='darwin-viewer/dssat/get-ens-values',
                controller='darwin_viewer.ajax_controllers.get_ens_values'
            ),
            UrlMap(
                name='dsyield',
                url='darwin-viewer/dssat/get-schema-yield',
                controller='darwin_viewer.ajax_controllers.get_schema_yield'
            ),
            # UrlMap(
            #     name='get-vars',
            #     url='darwin-viewer/get-vars',
            #     controller='darwin_viewer.ajax_controllers.get_vars'
            # ),
        )

        return url_maps
