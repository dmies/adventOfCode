from day12 import Moon, simulate_moons


def test_init_handles_string_input():
    line = "<x=15, y=-2, z=-6>"

    expected_x = 15
    expected_y = -2
    expected_z = -6
    result = Moon(line)

    assert result.x == expected_x
    assert result.y == expected_y
    assert result.z == expected_z


def test_apply_velocity():
    # x=1, y=2, z=3 and a velocity of x=-2, y=0,z=3, then its new position would be x=-1, y=2, z=6
    moon = Moon("<x=1, y=2, z=3>")
    moon.velocity = (-2, 0, 3)
    expected = Moon("<x=-1, y=2, z=6>")
    expected.velocity = (-2, 0, 3)
    moon.apply_velocity()
    assert moon == expected


def test_simulate_moons():
    expected_input = [
        "<x= 2, y=-1, z= 1>",
        "<x= 3, y=-7, z=-4>",
        "<x= 1, y=-7, z= 5>",
        "<x= 2, y= 2, z= 0>",
    ]

    expected = [Moon(row) for row in expected_input]

    start_input = [
        "<x=-1, y=  0, z= 2>",
        "<x= 2, y=-10, z=-7>",
        "<x= 4, y= -8, z= 8>",
        "<x= 3, y=  5, z=-1>",
    ]

    moons = [Moon(row) for row in start_input]
    for moon in moons:
        print(f"{moon}")
    moons = simulate_moons(moons)
    print("---")
    for moon in moons:
        print(f"{moon}")
    assert moons == expected

