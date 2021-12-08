# Linear-filter-function
applying 3x3 linear filter on a grey-scale image of NxM pixels

The function takes the following as inputs,

1. The filter 3x3 filter mask as a 3x3 integer array
2. Input image
3. A parameter specifying how the edge pixels should be treated (O- omit edge pixels, S- shrink filter at edges, P-pad the image with black white coloured pixels, R-replicate edge rows and W-wrap the image

The function outputs the image as a result.
