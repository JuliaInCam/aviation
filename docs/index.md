# Welcome to Julia's MkDocs

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.

# Aviation
Simple model of global aviation.

## Docs

The "required global fleet" can be estimated using a very simple model that assumes the number of passengers flying globally annually is known, along with an estimation of the number of seats flown globally per day.

## Constants

| True constant | Value | Unit     |
| :---          | :----:|     ---: |
| days per year | 365   |       .  |

| Inputs | Value | Unit     | Source |
| :---   | :---  |   :---   |  :---  |
| passengers per year  | $5 \times 10^9$   | $\text{year}^{-1}$ | ATAG[^1] |
|  seats per aircraft | $150$   | . |  |
|  flights per aircraft per day  | $2$   | $\text{day}^{-1}$ |  |

## Equations
Given that the two sources inputs that are time dependent are given in different time bases, it is convenient to convert one of these two are consistent.

$\text{passsengers per day} = \frac{\text{passengers per year}}{\text{days per year}}$

The total required global fleet can then be calcualted as a function of this intermediate value and the other inputs.

$\text{required global fleet} = \frac{\text{passengers per day}}{\text{seats per aircraft } \times \text{ flights per aircraft per day}}$

[^1]: Reference 
