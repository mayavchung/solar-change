Code is executed in order 0, 1, 2. 0 will need to be adapted to local workflow.

This code uses the GFDL radiative kernel from [Soden et al. (2008)](https://journals.ametsoc.org/view/journals/clim/21/14/2007jcli2110.1.xml) which can be downloaded [here](https://climate.rsmas.miami.edu/data/radiative-kernels/).

These scripts are based on code by Chenggong Wang. Further details and original code are available [here](https://github.com/ChenggongWang/Radiative_Response_with_Radiative_Kernel).

./total_feedback/ contains the total estimated feedbacks plotted in Figure 2.

Residual feedbacks are in resid_feedback_results.nc (plotted in 2_plot_feedbacl_decomp_GFDL_cloud.ipynb).
