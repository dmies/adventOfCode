from day12 import Moon, simulate_moons, get_steps_to_find_same_state


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


def test_get_steps_to_find_same_state():
    expected = 4686774924
    start_input = [
        "<x=-8, y=-10, z=0>",
        "<x=5, y=5, z=10>",
        "<x=2, y=-7, z=3>",
        "<x=9, y=-8, z=-3>",
    ]
    moons = [Moon(row) for row in start_input]

    result = get_steps_to_find_same_state(moons)
    assert result == expected

