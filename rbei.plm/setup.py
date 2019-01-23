from cdb.comparch.pkgtools import setup

setup(
    name="rbei.plm",
    version="1.0.0",
    install_requires=['cs.actions', 'cs.activitystream', 'cs.base', 'cs.bomcreator', 'cs.defects', 'cs.designsystem', 'cs.documents', 'cs.ec', 'cs.launchpad', 'cs.metrics', 'cs.officelink', 'cs.pcs', 'cs.platform', 'cs.portfolios', 'cs.powerreports', 'cs.taskmanager', 'cs.vp', 'cs.vp-pcs', 'cs.web', 'cs.workflow', 'cs.workspaces', 'cscdb.product'],
    docsets=[
        # Add a relative path for each documentation set in this package
        ],
    cdb_modules=[
        # List the package's modules in the correct (initialization) order as
        # computed by cdb.comparch topological sort. This list goes into
        # `cdb_modules.txt` in the EGG-INFO.
        "rbei.plm"
        ],
    cdb_services=[
        # List the services of this packages by their class names. This list
        # goes into `cdb_services.txt` in EGG-INFO.
        ],
)
