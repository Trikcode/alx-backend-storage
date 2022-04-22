-- SQL script that lists all bands with Glam rock as their main style, ranked by their longevity
-- Column names must be: band_name and lifespan (in years)
-- use attributes formed and split for computing the lifespan

SELECT band_name, COALESCE(split, 2020) - formed as lifespan FROM
metal_bands WHERE style LIKE '%Glam rock%' ORDER BY lifespan DESC;
